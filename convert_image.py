from PIL import Image
import pillow_avif

def convert_avif_to_png(input_path, output_path):
  """
  Converts an AVIF image to PNG format.

  Args:
    input_path: Path to the input AVIF image.
    output_path: Path to save the output PNG image.
  """
  try:
    img = Image.open(input_path)
    img.save(output_path, "PNG")
    print(f"Successfully converted {input_path} to {output_path}")
  except Exception as e:
    print(f"An error occurred: {e}")

if __name__ == "__main__":
  input_image = "/home/marco/Scrivania/SMASH/De-novo-nanobody-re-design/Images/Background.avif"
  output_image = "/home/marco/Scrivania/SMASH/De-novo-nanobody-re-design/Images/Background.png"
  convert_avif_to_png(input_image, output_image)
