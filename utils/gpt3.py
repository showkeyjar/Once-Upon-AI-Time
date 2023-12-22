import openai
import logging

logging.root.setLevel(logging.NOTSET)
logging.basicConfig(format="%(thread)d %(asctime)s %(name)s:%(levelname)s:%(lineno)d:%(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S", level=logging.DEBUG)
logging.getLogger("openai").setLevel(logging.ERROR)
logger = logging.getLogger(__name__)

openai.api_key = "sk-foaMP2VokxeMoK6WKdQok2CQMIuUNjukgffxtof2urdiAbsx"
# openai.api_base = "http://localhost:3000/v1"
openai.api_base = "http://127.0.0.1:5000/v1"


def generate_with_prompt(prompt: str, temperature: float) -> str:
    """
    Generate text given input prompt.
    
    Args:
        prompt: Input prompt
        temperature: Temperature of generation

    Returns:
        output

    Raises:
        RuntimeError: Failed to generate
    """
    # Generate story
    response = openai.Completion.create(
        # model="text-davinci-002",
        model="all-mpnet-base-v2",
        prompt=prompt,
        temperature=temperature,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    output = response["choices"][0].text

    # Content filtered story
    # 由于text-gen-ui 暂不支持, 所以先不实现
    # response = openai.Completion.create(
    #     engine="content-filter-alpha",
    #     prompt="<|endoftext|>" + output + "\n--\nLabel:",
    #     temperature=0,
    #     max_tokens=1,
    #     top_p=0,
    #     logprobs=10,
    # )
    # output_label = response["choices"][0].text

    # Regenerate story if failed content filter or story too short
    # if int(output_label) < 2:
    logger.debug("input: " + prompt)
    logger.debug("output: " + output)
    return output

    # raise RuntimeError("Failed to generate")
