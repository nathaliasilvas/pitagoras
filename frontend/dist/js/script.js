function handleCalculate(e) {
    e.preventDefault()
    const a = document.querySelector('#a').value
    const b = document.querySelector('#b').value

    calculate(a, b).then((response) => {
        const result = document.querySelector('#result-span')
        result.innerHTML = response.result ?? 0
        result.parentElement.parentElement.classList.remove('d-none')
    })
}

async function calculate(a, b) {
    const params = new URLSearchParams({ a, b })
    const data = await fetch(`http://localhost:5000/calculator?${params}`)

    return data.json()
}

document.querySelector('#calculator').addEventListener('submit', handleCalculate)
