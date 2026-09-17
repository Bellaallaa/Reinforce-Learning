const $ = id => document.getElementById(id);
$('study').addEventListener('click', () => {
  const active = document.body.classList.toggle('study');
  $('study').setAttribute('aria-pressed', String(active));
  $('study').textContent = active ? '显示全部解析' : '自测模式';
  document.querySelectorAll('.solution').forEach(el => el.open = !active);
});
let printState;
window.addEventListener('beforeprint', () => {
  printState = [...document.querySelectorAll('details')].map(el => [el, el.open]);
  printState.forEach(([el]) => el.open = true);
});
window.addEventListener('afterprint', () => printState?.forEach(([el, open]) => el.open = open));
$('print').addEventListener('click', () => window.print());
function updateEpsilon() {
  const eps = Number($('epsilon').value), n = Number($('actions').value);
  $('eps-out').textContent = eps.toFixed(2);
  if (!Number.isInteger(n) || n < 2 || n > 100) {
    $('eps-result').textContent = '请输入 2–100 之间的整数。';
    $('exploit').style.width = $('explore').style.width = '0%';
    return;
  }
  const direct = 1-eps, random = eps/n;
  $('exploit').style.width = `${direct*100}%`;
  $('explore').style.width = `${random*100}%`;
  $('eps-result').textContent = `P(贪心) = ${direct.toFixed(4)} + ${random.toFixed(4)} = ${(direct+random).toFixed(4)}；每个非贪心动作的概率 = ${random.toFixed(4)}。`;
}
function updateGamma() {
  const gamma = Number($('gamma').value);
  $('gamma-out').textContent = gamma.toFixed(2);
  const weights = Array.from({length:10}, (_,i) => gamma**i);
  $('discount-bars').replaceChildren(...weights.map(w => {
    const bar = document.createElement('span'); bar.style.height = `${w*100}%`; return bar;
  }));
  $('gamma-result').textContent = `前 10 步回报 = ${weights.reduce((a,b)=>a+b,0).toFixed(4)}；无限时域回报 = ${gamma===1?'∞（每步奖励为 1，级数发散）':(1/(1-gamma)).toFixed(4)}。`;
}
['epsilon','actions'].forEach(id => $(id).addEventListener('input',updateEpsilon));
$('gamma').addEventListener('input',updateGamma);
updateEpsilon(); updateGamma();
