# ORM Map Generator

Python script to automatically combine ambient occlusion, roughness, and metalness grayscale textures from an 'in' directory into ORM maps saved in an 'out' directory.

## Usage

1. Place your ambient occlusion, roughness, and (optionally) metalness textures in the `in` directory. The script expects the textures to be named with the following pattern:
   - `YourTextureName_AmbientOcclusion.png`
   - `YourTextureName_Roughness.png`
   - `YourTextureName_Metalness.png`

2. Run the script:
   ```bash
   python main.py

