# SPDX-FileCopyrightText: 2025 QinHan
# SPDX-License-Identifier: MPL-2.0
"""
Vercel Serverless Function Entry Point for DocuTranslate

Note: Vercel has execution time limits:
- Hobby: 10 seconds
- Pro: 60 seconds
- Enterprise: 300 seconds

For long-running translation tasks, consider using the async endpoints
with polling, or use an external queue service.
"""
import os
import sys
from pathlib import Path

# Add parent directory to path to import docutranslate
sys.path.insert(0, str(Path(__file__).parent.parent))

from mangum import Mangum
from docutranslate.app import create_app

# Create FastAPI app instance with CORS enabled for web access
app = create_app(enable_cors=True, allow_origin_regex=r"^https?://.*$")

# Create Mangum handler for Vercel
# lifespan="off" because Vercel serverless functions don't support lifespan events
handler = Mangum(app, lifespan="off")

def lambda_handler(event, context):
    """
    AWS Lambda / Vercel handler
    This function is called by Vercel for each request
    """
    return handler(event, context)
