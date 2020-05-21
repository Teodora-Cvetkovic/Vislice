% import model
<!DOCTYPE html>
<html>

<body>

  <h1>Vislice</h1>

  <blockquote>
    Vislice so najboljša igra za preganjanje dolgčasa (poleg tetrisa).
    <small>Študentje</small>
  </blockquote>

  <table>
    <tr>
      <td>
        <h2>{{igra.pravilini_del_gesla()}}</h2>
      </td>
    </tr>
    <tr>
      <td>
        Nepravilni ugibi: {{igra.nepravilni_ugibi()}}
      </td>
    </tr>
    <tr>
      <td>
        <img src="/img/{{igra.stevilo_napak()}}.jpg" alt="obešanje">
      </td>
    </tr>
  </table>
    
  % if poskus == model.ZMAGA:
  <h1>ZMAGA!!!</h1>
  <form action="/igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>

  % elif poskus == model.PORAZ:
  <h1>BUUUUU!!! LOSER!!!</h1>
  Pravilno geslo: {{igra.geslo}}
  <form action="/igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>

  % else:
  <form action="/igra/{{id_igre}}/" method="post">
    Črka <input type="text" name="crka">
    <button type="submit">Pošlji</button>
  </form>

</body>

</html>