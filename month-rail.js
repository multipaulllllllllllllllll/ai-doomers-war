(() => {
  const ledger = document.querySelector('.ledger');
  if (!ledger) return;
  const months = [...ledger.querySelectorAll(':scope > details')];
  const track = document.createElement('div');
  track.className = 'month-rail'; track.setAttribute('role','group'); track.setAttribute('aria-label','Choose a month');
  const buttons = months.map((panel,i) => {
    const button = document.createElement('button'); button.type='button';
    button.setAttribute('aria-controls', panel.id);
    for(const [cls, text] of [['rail-month',panel.querySelector('summary .month').textContent],['rail-title',panel.querySelector('summary i').textContent],['rail-count',panel.querySelectorAll('article.tl-content').length+' entries']]) {
      const span=document.createElement('span'); span.className=cls; span.textContent=text; button.append(span);
    }
    button.onclick=()=>select(panel.open ? -1 : i);
    panel.addEventListener('toggle',()=>button.setAttribute('aria-expanded',String(panel.open)));
    panel.querySelector('summary').addEventListener('click',e=>{e.preventDefault();select(-1);button.focus()});
    track.append(button); return button;
  });
  function select(i){months.forEach((p,j)=>{p.open=i===j;buttons[j].setAttribute('aria-expanded',String(p.open))});}
  function syncHash(){
    const target=document.getElementById(location.hash.slice(1));
    const linked=months.findIndex(p=>target && p.contains(target));
    const i=linked>=0 ? linked : months.findIndex(p=>p.id==='month-2026-11');
    select(i);
    if(i>=0) track.scrollLeft+=buttons[i].getBoundingClientRect().left-track.getBoundingClientRect().left;
    if(linked>=0) target.scrollIntoView({block:'start',behavior:'instant'});
  }
  ledger.before(track);ledger.classList.add('rail-panels');syncHash();window.addEventListener('hashchange',syncHash);
})();
