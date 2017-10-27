
function myfunction() {
  console.log('hello there');
  a = document.getElementById('actual-menu').innerHTML;
  console.log(a);

}

function setDivVisible(id) {
  document.getElementById(id).style.visibility='visible';
}

function setDivHidden(id) {
  document.getElementById(id).style.visibility='hidden';
}

function insertRawInTable(id, nf) {
  var table = document.getElementById(id);
  var raw = table.insert(-1);
  var cell1 = table.insert(1);
}

function a() {
  insertRawInTable("tabl", 0)
}
