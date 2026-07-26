import torch
import torch.nn as nn
import torch.nn.functional as F

class ConvBlock(nn.Module):
    def __init__(
        self,
        in_channels,
        out_channels,
        kernel_size=3,
        stride=1,
        padding=1,
        batchnorm=True,
        dropout_rate=0.0,
    ):
        super(ConvBlock, self).__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(
                in_channels,
                out_channels,
                kernel_size=kernel_size,
                stride=stride,
                padding=padding,
            ),
            nn.BatchNorm2d(num_features=out_channels) if batchnorm else nn.Identity(),
            nn.ReLU(inplace=True),
            nn.Dropout2d(p=dropout_rate),
            nn.Conv2d(
                out_channels,
                out_channels,
                kernel_size=kernel_size,
                stride=stride,
                padding=padding,
            ),
            nn.BatchNorm2d(num_features=out_channels) if batchnorm else nn.Identity(),
            nn.ReLU(inplace=True),
            nn.Dropout2d(p=dropout_rate),
        )

    def forward(self, x):
        return self.conv(x)

class Encoder(nn.Module):
    def __init__(self, in_channels, batchnorm, dropout_rate=0.0):
        super(Encoder, self).__init__()
        self.conv_blocks = nn.ModuleList(
            [
                ConvBlock(
                    in_channels=in_channels,
                    out_channels=64,
                    batchnorm=batchnorm,
                    dropout_rate=dropout_rate,
                ),
                ConvBlock(
                    in_channels=64,
                    out_channels=128,
                    batchnorm=batchnorm,
                    dropout_rate=dropout_rate,
                ),
                ConvBlock(
                    in_channels=128,
                    out_channels=256,
                    batchnorm=batchnorm,
                    dropout_rate=dropout_rate,
                ),
                ConvBlock(
                    in_channels=256,
                    out_channels=512,
                    batchnorm=batchnorm,
                    dropout_rate=dropout_rate,
                ),
            ]
        )
        self.max_pool = nn.MaxPool2d(kernel_size=2, stride=2)

    def forward(self, x):
        skip_connections = []
        for conv_block in self.conv_blocks:
            x = conv_block(x)
            skip_connections.append(x)
            x = self.max_pool(x)
        return x, skip_connections

class Bottleneck(nn.Module):
    def __init__(self, in_channels=512, out_channels=1024, batchnorm=True, dropout_rate=0.0):
        super(Bottleneck, self).__init__()
        self.bottleneck = ConvBlock(
            in_channels=in_channels,
            out_channels=out_channels,
            batchnorm=batchnorm,
            dropout_rate=dropout_rate
        )

    def forward(self, x):
        return self.bottleneck(x)


class UpConvBlock(nn.Module):
    def __init__(self, in_channels, out_channels, batchnorm=True, dropout_rate=0.0):
        super(UpConvBlock, self).__init__()
        self.up = nn.ConvTranspose2d(in_channels, out_channels, kernel_size=2, stride=2)
        
        self.conv_block = ConvBlock(
            in_channels=out_channels * 2,
            out_channels=out_channels,
            batchnorm=batchnorm,
            dropout_rate=dropout_rate
        )

    def forward(self, x, skip_x):
        x = self.up(x)
        diffY = skip_x.size()[2] - x.size()[2]
        diffX = skip_x.size()[3] - x.size()[3]
        x = F.pad(x, [diffX // 2, diffX - diffX // 2,
                      diffY // 2, diffY - diffY // 2])
        x = torch.cat([x, skip_x], dim=1)
        return self.conv_block(x)


class Decoder(nn.Module):
    def __init__(self, batchnorm=True, dropout_rate=0.0):
        super(Decoder, self).__init__()
        self.up1 = UpConvBlock(in_channels=1024, out_channels=512, batchnorm=batchnorm, dropout_rate=dropout_rate)
        self.up2 = UpConvBlock(in_channels=512, out_channels=256, batchnorm=batchnorm, dropout_rate=dropout_rate)
        self.up3 = UpConvBlock(in_channels=256, out_channels=128, batchnorm=batchnorm, dropout_rate=dropout_rate)
        self.up4 = UpConvBlock(in_channels=128, out_channels=64, batchnorm=batchnorm, dropout_rate=dropout_rate)

    def forward(self, x, skip_connections):
        x = self.up1(x, skip_connections[3])
        x = self.up2(x, skip_connections[2])
        x = self.up3(x, skip_connections[1])
        x = self.up4(x, skip_connections[0])
        return x


class FinalConv(nn.Module):
    def __init__(self, in_channels, num_classes):
        super(FinalConv, self).__init__()
        self.conv = nn.Conv2d(in_channels, num_classes, kernel_size=1)

    def forward(self, x):
        return self.conv(x)


class UNet(nn.Module):
    def __init__(self, in_channels=3, num_classes=1, dropout_rate=0.0, batchnorm=True):
        super(UNet, self).__init__()
        self.encoder = Encoder(in_channels, batchnorm, dropout_rate=dropout_rate)
        self.bottleneck = Bottleneck(512, 1024, batchnorm, dropout_rate)
        self.decoder = Decoder(batchnorm, dropout_rate)
        self.final_conv = FinalConv(64, num_classes)

    def forward(self, x):
        output, skip_connections = self.encoder(x)
        output = self.bottleneck(output)
        output = self.decoder(output, skip_connections)
        output = self.final_conv(output)
        return output