#!/usr/bin/env python3
"""
Convert various document formats to Markdown using markitdown tool.

This script uses Microsoft's markitdown tool to convert documents (PDF, DOCX, XLSX, PPTX, etc.)
to markdown format suitable for AI processing.

Usage:
    python convert_to_markdown.py <file_path>
    
The output is printed to stdout for direct consumption by AI.
"""

import subprocess
import sys
import os


def main():
    if len(sys.argv) < 2:
        print("Usage: python convert_to_markdown.py <file_path>", file=sys.stderr)
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}", file=sys.stderr)
        sys.exit(1)
    
    # Supported file extensions
    supported_extensions = {
        '.pdf', '.docx', '.doc', '.xlsx', '.xls', '.pptx', '.ppt',
        '.html', '.htm', '.xml', '.json', '.csv', '.zip'
    }
    
    # Check file extension
    _, ext = os.path.splitext(file_path)
    if ext.lower() not in supported_extensions:
        print(f"Warning: File extension '{ext}' may not be fully supported by markitdown", file=sys.stderr)
    
    try:
        # Run markitdown command
        # Using subprocess to call markitdown directly
        result = subprocess.run(
            ['markitdown', file_path],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Output to stdout
        print(result.stdout)
        
    except subprocess.CalledProcessError as e:
        print(f"Error converting file: {e.stderr}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print("Error: markitdown not found. Please ensure it is installed and activated.", file=sys.stderr)
        print("Installation: conda activate markitdown", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
