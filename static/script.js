document.getElementById('generate-btn').addEventListener('click', () => {
    fetch('/generate')
        .then(response => response.json())
        .then(data => {
            document.getElementById('mnemonic-output').innerText = data.words;
        })
        .catch(error => console.error('Error:', error));
});
