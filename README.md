# iPhoto Exporter

Export master images from an iPhoto Library.

I recently stumbled upon an old iPhoto library which contained a damaged database file. Fortunately each iPhoto library also contains an XML version of the library that can be parsed (at least in my case).

This Python module allows you to export the master images (i.e. unmodified originals) from an iPhoto Library by simply providing the path to an iPhoto Library file, and an output directory to which to copy the images.

Simply install the script with

```bash
pip install iphoto-exporter

```

and run the following to see the input/output arguments.

```bash
iphoto_exporter --help
```

## Todo

Additional features are imaginable, for example

* Only export certain albums by title/name
* Improve the progress bar
* Prevent duplicate images contained in multiple albums
* ...