import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO #bytes io used for buffer memory to store or capture images )


def load_image_from_url(url):
      response = requests.get(url)
      return Image.open(BytesIO(response.content))

elephant_url = "https://cdn.britannica.com/72/272-050-E1965E27/African-elephant-Kenya.jpg"
#elephant_url = "https://m.media-amazon.com/images/I/81JSw5mE54L._UF894,1000_QL80_.jpg"

elephant = load_image_from_url(elephant_url)


# display an original image
plt.figure(figsize=(6,4))
plt.imshow(elephant)
plt.title('Elephant')
plt.axis( 'off')

plt.show()

# image to array
elephant_np = np.array(elephant)
print('Elephant Image shape', elephant_np.shape)

# Convert to grayscale
elephant_gray = elephant.convert("L")

# Display grayscale image
plt.figure(figsize=(6, 4))
plt.imshow(elephant_gray, cmap="gray")
plt.title("Elephant (Grayscale)")
plt.axis("off")
plt.show()
