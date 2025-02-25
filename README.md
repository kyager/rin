# Rin

Rin is a command-line tool that interacts with OpenAI's API to send messages, files, or directory contents and receive responses.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/kyager/rin.git
    cd rin
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Create a [.env](.env) file based on the [.env.example](.env.example) file and set your OpenAI API key and model:
    ```sh
    cp .env.example .env
    # Edit .env to include your OpenAI API key and model
    ```

## Usage

Run the [rin.py](rin.py) script with the following arguments:

```sh
python rin.py [options] <message>
```

### Arguments

- `<message>`: The message to send to OpenAI. This argument is required unless `--file` or `--directory` is specified.

### Options

- `-f, --file <file>`: Send the contents of a file to OpenAI
- `-d, --directory <directory>`: Send the structure of a directory to OpenAI
- `-m, --model <model>`: Specify which OpenAI model to use (overrides .env setting)
- `-v, --verbose`: Enable verbose output mode
- `-h, --help`: Show help message and exit

## Examples

Send a simple message:
```sh
python rin.py "What is the capital of France?"
```

Send the content of a file:
```sh
python rin.py -f path/to/file
```

Send a directory structure with a specific model:
```sh
python rin.py -d ./project
```

## Environment Variables

Create a `.env` file with the following variables:

```ini
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4-turbo-preview
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.