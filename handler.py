from PIL import Image
import uuid

def handler(event):
    # Just create a solid color image (512x512)
    img = Image.new("RGB", (512, 512), "skyblue")

    # Save to /output with a unique name
    filename = f"{uuid.uuid4().hex}.png"
    path = f"/output/{filename}"
    img.save(path)

    return {
        "image_url": f"/output/{filename}"
    }
