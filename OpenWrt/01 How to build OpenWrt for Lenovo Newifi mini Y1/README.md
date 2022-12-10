# How to build OpenWrt for Lenovo Newifi mini Y1?

Build Host: Ubuntu 22.04

Target Model: Lenovo Y1

Target Processor: MediaTek MT7620A


![my newifi mini y1](https://github.com/mingwu1214/medium/blob/main/OpenWrt/01%20How%20to%20build%20OpenWrt%20for%20Lenovo%20Newifi%20mini%20Y1/Images/0%20Newifi%20mini%20Y1.jpg)

 Newifi mini Y1 is Lenovo’s phase-out wifi AP product, but it is still an excellent platform to practice building the OpenWrt firmware.

 Following is a hands-on procedure as your first step to familiarize yourself with building OpenWrt firmware.

```
git clone https://github.com/openwrt/openwrt.git
```

![git clone openwrt](https://github.com/mingwu1214/medium/blob/main/OpenWrt/01%20How%20to%20build%20OpenWrt%20for%20Lenovo%20Newifi%20mini%20Y1/Images/01%20git%20clone%20openwrt.png)

```
sudo apt-get update
sudo apt-get install subversion build-essential libncurses5-dev zlib1g-dev gawk git ccache gettext libssl-dev xsltproc
```
![git apt-get install](https://github.com/mingwu1214/medium/blob/main/OpenWrt/01%20How%20to%20build%20OpenWrt%20for%20Lenovo%20Newifi%20mini%20Y1/Images/02%20apt%20get%20install%20packages.png)

```
make package/symlinks
```
![make package/symlinks](https://github.com/mingwu1214/medium/blob/main/OpenWrt/01%20How%20to%20build%20OpenWrt%20for%20Lenovo%20Newifi%20mini%20Y1/Images/03%20make%20package%20symlinks.png)


```
make menuconfig
```

## Select “Target System” -> “MediaTek Ralink MIPS”
![Select “Target System” -> “MediaTek Ralink MIPS”](https://github.com/mingwu1214/medium/blob/main/OpenWrt/01%20How%20to%20build%20OpenWrt%20for%20Lenovo%20Newifi%20mini%20Y1/Images/04%20menuconfig%20target%20system.png)

## Select “Target Profile” -> “Lenovo Y1”
![Select “Target Profile” -> “Lenovo Y1”](https://github.com/mingwu1214/medium/blob/main/OpenWrt/01%20How%20to%20build%20OpenWrt%20for%20Lenovo%20Newifi%20mini%20Y1/Images/05%20menuconfig%20target%20profile.png)

## Select “LuCI” -> “Collections” -> “luci”
![Select “LuCI” -> “Collections” -> “luci”](https://github.com/mingwu1214/medium/blob/main/OpenWrt/01%20How%20to%20build%20OpenWrt%20for%20Lenovo%20Newifi%20mini%20Y1/Images/06%20menuconfig%20luci.png)

```
make V=99
```
![make V=99](https://github.com/mingwu1214/medium/blob/main/OpenWrt/01%20How%20to%20build%20OpenWrt%20for%20Lenovo%20Newifi%20mini%20Y1/Images/07%20make.jpg)

```
cd bin/targets/ramips/mt7620
ls -al
```
![target images](https://github.com/mingwu1214/medium/blob/main/OpenWrt/01%20How%20to%20build%20OpenWrt%20for%20Lenovo%20Newifi%20mini%20Y1/Images/08%20Target%20Images.png)

## References:
[[1] OpenWRT — Techdata: Lenovo Newifi mini Y1](https://openwrt.org/toh/hwdata/lenovo/lenovo_newifi_mini_y1)

