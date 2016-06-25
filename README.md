# RSRCExtractor

This fork allows you to extract any resource type, as raw binary data.

Some notes:

- Files are currently saved in output/ directory
- PICT resources get .pict extension appended

##Original README:

What is this?

A python script to pull out PICT data from files with Mac Resource forks

Why?

There's nothing else like this out there that I can find.

How?

https://en.wikipedia.org/wiki/Resource_fork explains the concept of a
Resource Fork. One of the items in the Resource Fork is a PICT resource.
This is litterally a PICT file minus the 512 byte header. The PICT file
is really poorly documented but that's not actually important for getting
it out. The basic steps here are

1) Run DeRez on the file to extract the PICT data
2) Parse the PICT data
3) add a 512 byte header of zeros, stick it in a binary file with .pct
4) Open with Preview
5) Save your image to a more modern format

What do I need?

- Python
- Apple Developer tools with DeRez

How to use?

python <path to file with resource fork>

Isn't this kind of a hackjob?

You betcha. The hope is that this will be useful to someone else who is
poking at ancient mac files.
