if not image_meta_tag:
        return "No meta tag with property 'og:image' was found."

    image_url = image_meta_tag.get("content")
    if not image_url:
        return f"Image URL not found in meta tag {image_meta_tag}."#nice

    try:
        image_data = requests.get(image_url).content
    except requests.exceptions.RequestException as e:
        return f"An error occurred during the HTTP request to {image_url}: {e!r}"
    if not image_data:
        return f"Failed to download the image from {image_url}."

    file_name = f"{datetime.now():%Y-%m-%d_%H:%M:%S}.jpg"
    with open(file_name, "wb") as out_file:
        out_file.write(image_data)
    return f"Image downloaded and saved in the file {file_name}"#hello

def download_video(url: str) -> bytes:
    base_url = "https://downloadgram.net/wp-json/wppress/video-downloader/video?url="
    video_url = requests.get(base_url + url).json()[0]["urls"][0]["src"]
    return requests.get(video_url).content
