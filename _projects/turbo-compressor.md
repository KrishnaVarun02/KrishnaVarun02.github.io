---
layout: project
title: Turbo Compressor
subtitle: Lossless Huffman Compression CLI
excerpt: A C++ command-line utility for lossless file compression and decompression using Huffman coding.
project_slug: turbo-compressor
permalink: /projects/turbo-compressor/
order: 2
published: true
featured: false
supervisors: [Prof. Dr. Bhaskar Biswas]
tags: [C++, Huffman coding, Data structures, Object-oriented programming, CLI]
image: ''
image_alt: ''
repository_url: 'https://github.com/KrishnaVarun02/Turbo-Compressor'
demo_url: ''
---

Turbo Compressor is a C++ command-line utility for lossless file compression and decompression using Huffman coding. The project applies data structures and algorithm design to binary file encoding while preserving the original contents.

## Compression and decompression

- Analyzes symbol frequencies and uses a priority queue to construct a Huffman tree.
- Generates prefix codes and performs bit-level encoding and decoding.
- Reconstructs original files byte-for-byte without information loss.

## Design

A modular object-oriented design separates compression, decoding, tree management, and file handling. The implementation uses priority queues, binary trees, and bit manipulation to organize the encoding and reconstruction process.
