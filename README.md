
# Zoe Depth Estmiation

A brief description of what this project does and who it's for


## Usage/Examples

### CLI Usage
```javascript
cli.py [-h] [--print-settings] [input_image] [output_image]

Depth estimation using ZoeDepth.

positional arguments:
  input_image       Path to input image.
  output_image      Path to output depth map.

options:
  -h, --help        show this help message and exit
  --print-settings  Print the default settings and exit.
```
###API USAGE

http://127.0.0.1:8000/docs then predict

## Installation

Install depth estimation project with npm

```bash
pip install -r requirements.txt

```
    
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

`ANOTHER_API_KEY`


## Deployment

To deploy this project run

```bash
  npm run deploy
```


## License

[MIT](https://choosealicense.com/licenses/mit/)

