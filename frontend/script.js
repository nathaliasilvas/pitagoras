function handleCalculate() {
    const a = document.querySelector('#a').value
    const b = document.querySelector('#b').value

    calculate(a, b).then((response) => {
        document.querySelector('#result-span').innerHTML = response.result ?? 0
        document.querySelector('#result').classList.remove('d-none')
    })
}

async function calculate(a, b) {
    const params = new URLSearchParams({ a, b })
    const data = await fetch(`http://localhost:5000/calculator?${params}`)

    return data.json()
}
