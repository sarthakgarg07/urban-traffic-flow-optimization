async function findShortestPath() {
    const origin = document.getElementById('origin').value;
    const destination = document.getElementById('destination').value;

    const response = await fetch(`/shortest-path?origin=${origin}&destination=${destination}`);
    const result = await response.json();

    document.getElementById('result').innerHTML = `Distance: ${result.distance}, Path: ${result.path.join(' -> ')}`;
}
