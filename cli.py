import argparse

def initialize_model(): # we have defined this as a function otherwise, this code starts automatically
    # and can  not import other functions such as --help or --print-settings
    from predictor import DepthEstimationModel
    return DepthEstimationModel()

def main():
    parser = argparse.ArgumentParser(description="Depth estimation using ZoeDepth.")
    parser.add_argument("input_image", nargs='?', help="Path to input image.")
    parser.add_argument("output_image", nargs='?', help="Path to output depth map.")
    parser.add_argument('--print-settings', action='store_true', help='Print the default settings and exit.')

    args = parser.parse_args()

    if args.print_settings:
        print_settings()
        return

    if args.input_image and args.output_image:
        model = initialize_model()
        result = model.calculate_depthmap(args.input_image, args.output_image)
        print(result)
    else:
        parser.print_help()

def print_settings():
    settings = {
        "model_name": "DepthEstimationModel",
        "input_format": "PNG, JPG",
        "output_format": "PNG",
    }
    print("Default Settings:")
    for key, value in settings.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
