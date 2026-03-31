def convert_to_uppercase(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
            content = infile.read()
            outfile.write(content.upper())
            
        print(f"Success! {input_filename} copied to {output_filename} in uppercase.")
        
    except FileNotFoundError:
        print("Error: Source file not found.")
    except Exception as e:
        print(f"Error: {e}")

convert_to_uppercase('source.txt', 'destination.txt')
