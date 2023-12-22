import hashlib
import webuiapi

negative_prompts = "nsfw, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry,  badhandv4, easynegative, ng_deepnegative_v1_75t, verybadimagenegative_v1.3"
# Load image model
api = webuiapi.WebUIApi(host='127.0.0.1', port=7861)


def generate_image(prompt: str) -> str:
    """
    Generate an image and get image link.

    Args:
        prompt for image

    Returns:
        image link

    Raises:
        Failed to generate image
    """
    global negative_prompts
    # todo 还需要找到合适的lora模型及参数, 目前的设置不符合古诗的风格
    result1 = api.txt2img(prompt=prompt,
                        negative_prompt=negative_prompts,
                        seed=1003,
                        styles=["anime"],
                        cfg_scale=7,
    #                      sampler_index='DDIM',
    #                      steps=30,
    #                      enable_hr=True,
    #                      hr_scale=2,
    #                      hr_upscaler=webuiapi.HiResUpscaler.Latent,
    #                      hr_second_pass_steps=20,
    #                      hr_resize_x=1536,
    #                      hr_resize_y=1024,
    #                      denoising_strength=0.4,

                        )
    md5 = hashlib.md5(prompt.encode('utf-8')).hexdigest()
    file_path = "output/" + md5 + ".png"
    result1.image.save(file_path)
    return file_path

