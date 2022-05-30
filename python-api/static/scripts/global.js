const jobArray = ['alergologia', 'cardiologia', 'dermatologia', 'endocrinologia', 'gastoenterologia', 'geriatria', 'hematologia', 'imunologia', 'infectologia', 'mastologia', 'nefrologia', 'neurologia', 'oftamologia', 'oncologia',
  'ortopedia', 'otorrinolaringologia', 'pediatria', 'pneumologia', 'proctologia', 'psiquiatria', 'reumatologia', 'traumatologia'
]

const jobOption = document.getElementById("especiality")

for (i = 0; i < jobArray.length; i++) {
  var especialidade = jobArray[i]
  especialidade = especialidade[0].toUpperCase() + especialidade.substr(1);

  opcao = document.createElement('OPTION')

  opcao.setAttribute("value", `${jobArray[i].toLowerCase()}`)
  var description = document.createTextNode(`${especialidade}`)
  opcao.appendChild(description)
  jobOption.appendChild(opcao)
}

function getDataUser() {
  
  username = document.getElementById('username').value
  job = document.getElementById('job').value
  cr = document.getElementById('cr').value
  especialty = document.getElementById('especiality')

  var especialty_value = especialty.options[especialty.selectedIndex].value;

  user = {
    "username": `${username}`,
    "especialty": `${especialty_value}`,
    "job": `${job}`,
    "cr": `${cr}`
  }
  return user
}