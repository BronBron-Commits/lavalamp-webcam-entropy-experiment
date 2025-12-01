# U-ai

U-ai is a small experimental AI project written in Rust.  
It provides a lightweight text interface and plugs into an external entropy source when available.

## Features

- Custom tokenizer system using SentencePiece.
- Simple command-line chat interface.
- Optional entropy integration using a named pipe.
- Small and easy-to-understand code layout.

## Running

cargo run -- "your message"

To start the interactive chat interface:

cargo run

## Entropy Integration

If a named pipe exists at:

    /tmp/unhidra_entropy.pipe

U-ai will attempt to read a single byte from it before generating a response.  
If the pipe is not available, U-ai falls back to pseudorandom behavior.

This design allows U-ai to connect to any external entropy “appliance.”

## Project Structure

- src/tokenizer – tokenization and SentencePiece bindings.
- src/entropy.rs – optional webcam/pipe entropy source.
- src/lib.rs – main logic.
- src/main.rs – CLI entry point.

## Requirements

- Rust toolchain
- SentencePiece C libraries installed
- Optional: entropy source (pipe) created by another program

## License

MIT License.
