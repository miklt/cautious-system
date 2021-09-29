import axios from 'axios'
// gateway para conexão com o backend
// pagina login -> api login -> backend/login.py

async function hora(req, res) {
  const horaAPI = await axios.get(
    'http://worldtimeapi.org/api/timezone/America/Sao_Paulo',
  )
  //console.log(horaAPI)
  return res.status(200).json({ hora_atual: horaAPI.data.datetime })
}
export default hora
