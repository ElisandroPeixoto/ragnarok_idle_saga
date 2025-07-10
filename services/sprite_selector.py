def get_char_image_by_job(job: str):
    """Return the image path by the character job"""

    job_image_map = {
        "Novice": "char_sprites/0.Novice_Sprite.png"
    }

    return job_image_map.get(job)
