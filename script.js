document.getElementById('checkButton').addEventListener('click', async () => {
  const address = document.getElementById('walletAddress').value.trim();
  const result = document.getElementById('result');
  
  if (!address) {
    result.textContent = "Please enter a wallet address.";
    return;
  }

  const response = await fetch('/check', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ address: address })
  });

  const data = await response.json();
  result.textContent = data.message;
});
