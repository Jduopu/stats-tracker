document.getElementById('playerForm').addEventListener('submit', async (e) => {
  e.preventDefault();

  const data = {
    name: document.getElementById('name').value,
    position: document.getElementById('position').value,
    touchdowns: parseInt(document.getElementById('touchdowns').value),
    yards: parseInt(document.getElementById('yards').value),
    tackles: parseInt(document.getElementById('tackles').value),
  };

  await fetch('/players', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });

  loadPlayers();
  e.target.reset();
});

async function loadPlayers() {
  const res = await fetch('/players');
  const players = await res.json();
  const tbody = document.getElementById('playerTable');
  tbody.innerHTML = '';
  players.forEach(p => {
    const row = `<tr>
      <td>${p.name}</td>
      <td>${p.position}</td>
      <td>${p.touchdowns}</td>
      <td>${p.yards}</td>
      <td>${p.tackles}</td>
    </tr>`;
    tbody.innerHTML += row;
  });
}

loadPlayers();
