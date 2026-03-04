---
name: markitdown
description: Convert various document formats (PDF, Word, Excel, PowerPoint, HTML, etc.) to markdown format suitable for AI processing. This skill should be used when the user requests to read, analyze, or extract content from documents in formats like PDF, DOCX, XLSX, PPTX, and other supported formats. Use this skill to transform documents into AI-friendly markdown before processing.
---

# Markitdown

## Overview

This skill enables document-to-markdown conversion using Microsoft's markitdown tool. Transform various document formats (PDF, Word, Excel, PowerPoint, HTML, etc.) into clean, structured markdown that is optimized for AI processing and analysis.

## When to Use This Skill

Use this skill when:
- User requests to read or analyze document content (PDF, DOCX, XLSX, PPTX, etc.)
- User needs to extract text or data from documents
- User wants to convert documents to a format suitable for AI processing
- User mentions document formats: PDF, Word, Excel, PowerPoint, HTML, XML, JSON, CSV, or ZIP files

## Supported Formats

The markitdown tool supports the following file formats:

- **Documents**: PDF (.pdf), Word (.docx, .doc)
- **Spreadsheets**: Excel (.xlsx, .xls), CSV (.csv)
- **Presentations**: PowerPoint (.pptx, .ppt)
- **Web**: HTML (.html, .htm), XML (.xml)
- **Data**: JSON (.json)
- **Archives**: ZIP (.zip) - extracts and processes contained files

## Quick Start

### Prerequisites

Ensure markitdown is installed and activated in the conda environment:

```bash
conda activate markitdown
```

### Basic Usage

Convert a document to markdown:

```bash
python scripts/convert_to_markdown.py <file_path>
```

The output is printed to stdout for direct AI consumption without creating intermediate files.

## Workflow

When the user requests document processing:

1. **Identify the document**: Determine the file path and format
2. **Check format support**: Verify the file format is supported
3. **Convert document**: Use `scripts/convert_to_markdown.py` to convert the document
4. **Process content**: Analyze the markdown output and respond to user's request

## Examples

### Example 1: Reading a PDF

**User request**: "Read this PDF file and summarize it"

**Action**:
```bash
python scripts/convert_to_markdown.py /path/to/document.pdf
```

The PDF content is converted to markdown and can be processed directly.

### Example 2: Extracting data from Excel

**User request**: "Extract the data from this Excel spreadsheet"

**Action**:
```bash
python scripts/convert_to_markdown.py /path/to/spreadsheet.xlsx
```

The Excel data is converted to markdown tables for easy parsing.

### Example 3: Analyzing a PowerPoint presentation

**User request**: "What are the main points in this PowerPoint?"

**Action**:
```bash
python scripts/convert_to_markdown.py /path/to/presentation.pptx
```

The presentation content is converted to markdown for analysis.

## Resources

### scripts/

**convert_to_markdown.py** - Main conversion script that wraps the markitdown tool.

- Accepts a file path as input
- Outputs markdown to stdout (no intermediate files)
- Includes error handling and format validation
- Supports all markitdown-compatible formats

## Advantages

- **No intermediate files**: Output goes directly to stdout for AI consumption
- **Broad format support**: Handles most common document formats
- **AI-friendly output**: Produces clean, structured markdown
- **Efficient processing**: Direct conversion without manual intervention

## Error Handling

The script includes comprehensive error handling:

- File existence validation
- Format support warnings
- Clear error messages for troubleshooting
- Installation instructions if markitdown is not found

## Installation

If markitdown is not installed:

```bash
# Using conda
conda activate markitdown

# Or install via pip
pip install markitdown
```

For more information, visit: https://github.com/microsoft/markitdown
