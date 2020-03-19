This challenge was pretty interesting. We start out just being given a pcap. After looking through the pcap with Wireshark I saw that there are some references to git and specifically protocols like x-git-pack-file-recieve. 

I looked through the packets which mentioned git a bit more carefully and saw some things which I expect when using git such as text like "Enumerating files 0/3". I looked for some more info on pack files and found the following [site](https://codewords.recurse.com/issues/three/unpacking-git-packfiles) which describes some important information about pack files. 
Here are the important take aways:
1. PACK is the magic header for a pack file
2. Pack files contain zlib compressed files
3. Pack files have corresponding idx files to tell where files are (for performance)

So using all of this I found a few packets with PACK file headers in them. Packet 76 was the packet that ended up having the correct PACK file that we care about. I saved the packet, carved it so that only the pack file is there without any header info (easy to do in Vim since the header is printable ascii and unique). Unix's file command recognizes it as a pack file now which is great. 

Next we know that the compressed files are zlib compressed data, so we can use binwalk to find those files in the pack and then extract them with `binwalk -e pack_file`. This also automatically uncompressed the zlib compressed data and put it into a folder. If we file all of those then we see that there is a jpg in there

```
100:      JPEG image data, JFIF standard 1.01, aspect ratio, density 72x72, segment length 16, baseline, precision 8, 413x549, frames 3
100.zlib: zlib compressed data
AD:       data
AD.zlib:  zlib compressed data
E:        ASCII text
E.zlib:   zlib compressed data
```

Viewing the image shows the flag!

![flag.jpg](https://github.com/Connor-McMillin/CTF-Write-Ups/tree/master/2020/angstrom/misc/ws3/flag.jpg)
