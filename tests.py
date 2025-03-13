import requests

def main():
    # The URL of your running FastAPI server
    url = f"http://127.0.0.1:12345/generate"

    # Text you want to synthesize
    text = """
    There's a snake in my boot.
    """

    # Prepare JSON payload
    payload = {
        "text": text.strip(),
        "voice": "am_santa",
        "language": "a",
        "speed": 1.2
        }

    # Send POST request to FastAPI server
    print("Sending request to /generate endpoint...")
    response = requests.post(url, json=payload)
    print(payload)

    if response.status_code == 200:
        # Save the returned audio as 'test_output.wav'
        output_filename = "test_output.wav"
        with open(output_filename, "wb") as f:
            f.write(response.content)
        print(f"Audio file saved as: {output_filename}")
    else:
        print(f"Request failed with status code {response.status_code}")
        print("Response text:", response.text)

if __name__ == "__main__":
    main()