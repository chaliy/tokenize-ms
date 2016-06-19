"""
Collection of microservices on top of tokenize-uk python module.

tokenize-uk uses regexes and rules to tokenize text into paragraphs,
paragraphs into sentences and sentences into words.
"""
from aiohttp import web
from validator import validate
from swagger import document
from tokenize_uk import tokenize_text
from schema import TOKENIZE_TEXT_OUTPUT_SCHEMA, TOKENIZE_TEXT_INPUT_SCHEMA

__author__ = "Dmitry Chaplinsky"
__copyright__ = "Copyright 2016, Dmitry Chaplinsky"
__credits__ = ["Dmitry Chaplinsky", "Vsevolod Dyomkin"]
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Dmitry Chaplinsky"
__email__ = "chaplinsky.dmitry@gmail.com"


@validate(
    input_schema=TOKENIZE_TEXT_INPUT_SCHEMA,
    output_schema=TOKENIZE_TEXT_OUTPUT_SCHEMA,
)
async def tokenize_text_handler(request, *args):
    """
    Tokenize given text into paragraphs, sentences and words.

    Endpoint uses Newline method to tokenize paragraphs and regexes and rules
    to tokenize sentences and words
    """
    return tokenize_text(request["text"])


app = web.Application()
app.router.add_route("POST", "/tokenize_text", tokenize_text_handler)

app = document(
    app,
    basePath="/",
    host="127.0.0.1:8080"
)

if __name__ == '__main__':
    web.run_app(app)
