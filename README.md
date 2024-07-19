# prxcheck

prxcheck is a Python-based proxy checker that verifies the functionality of HTTP and SOCKS proxies.

## Features

- **Protocol Support**: Supports HTTP and SOCKS proxies (versions 4, 4a, and 5).
## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/prxcheck.git
   ```

2. Navigate into the directory:

   ```bash
   cd prxcheck
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run prxcheck, use the following command:

```bash
python prxcheck.py 
```


### Example:

```bash
python prxcheck.py
1
proxies.txt
```

Replace `proxies.txt` with your list of proxies in IP:Port format.

## Proxy List Format

Ensure your proxy list (`proxies.txt`) you can change the filename to your desired:

```
192.168.0.1:8080
123.45.67.89:1080
```

Each line should contain one proxy in the format `IP:Port`.

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration
- etc.

---

Feel free to customize the sections based on additional features or specifics of your project.
