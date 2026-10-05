(()=>{const C=window.CODIGO,B=window.BLOCOS,$=s=>document.querySelector(s);
const esc=t=>t.replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));
const files=Object.keys(C),byId=Object.fromEntries(B.map(b=>[b.id,b]));let file=files[0],sel=null;
const rng=b=>C[b.arquivo].blocos[b.id];
const lines=b=>{const[i,j]=rng(b);return C[b.arquivo].src.split("\n").slice(i-1,j).map((t,k)=>[i+k,t])};
const notas=b=>(b.n||[]).map(([s,t])=>{const l=lines(b).find(x=>x[1].includes(s));return l?[l[0],t]:null}).filter(Boolean);
const chip=id=>`<button class="chip" data-id="${id}">${byId[id].nome} <small>${byId[id].arquivo}</small></button>`;
function render(){
 $("#files").innerHTML=files.map(f=>`<button class="file${f===file?" on":""}" data-f="${f}">${f}<small>${B.filter(b=>b.arquivo===f).length} blocos</small></button>`).join("");
 $("#chain").innerHTML=["main.py","desafio2.py","desafio1.py"].map(f=>`<div><span class="n${f===file?" on":""}">${f}</span></div>`).join("↓")+"<p>main.py usa converter (desafio2) e fmt/avaliar/tokenizar (desafio1). desafio2.py usa a Pilha de desafio1.</p>";
 $("#ftitle").textContent=file;
 const keys=sel?Object.fromEntries(notas(byId[sel])):{};
 $("#code").innerHTML=B.filter(b=>b.arquivo===file).sort((a,b)=>rng(a)[0]-rng(b)[0]).map(b=>`<article class="blk${sel===b.id?" on":""}" data-id="${b.id}" tabindex="0" role="button"><header><b>${b.nome}</b><em>${b.tipo}</em></header><div class="src">${lines(b).map(([n,t])=>`<div class="ln${sel===b.id&&keys[n]?" key":""}"><span>${n}</span><code>${esc(t)||" "}</code></div>`).join("")}</div></article>`).join("");
 const b=byId[sel];
 if(!b){$("#info").innerHTML="<h1>Explicação</h1><p class='tag'>Escolha um arquivo, depois clique em um bloco de código. A explicação aparece aqui.</p>";return}
 const sec=(t,x)=>`<h3>${t}</h3><p>${x}</p>`,lst=a=>a.length?a.map(chip).join(""):"<span class='none'>nenhum bloco</span>";
 $("#info").innerHTML=`<h1>${b.nome}</h1><div class="tag">${b.tipo} · ${b.arquivo} · linhas ${rng(b).join("–")}</div>`+
 sec("O que é?",b.e)+sec("Para que serve?",b.s)+sec("O que ela faz?",b.f)+sec("Como funciona?",b.c)+sec("O que recebe?",b.r)+sec("O que produz?",b.p)+
 `<h3>Utiliza (depende de)</h3>${lst(b.u)}<h3>Quem utiliza</h3>${lst(b.ub)}<h3>O que aconteceria se eu apagasse?</h3><p class="warn">${b.a}</p>`+sec("O que seria afetado?",b.i)+
 (notas(b).length?"<h3>Linhas importantes</h3>"+notas(b).map(([n,t])=>`<div class="note"><b>${n}</b><span>${t}</span></div>`).join(""):"");
}
document.addEventListener("click",e=>{const f=e.target.closest("[data-f]"),k=e.target.closest("[data-id]");
 if(f){file=f.dataset.f;sel=null;render();if(innerWidth>1000){$("#info").scrollTop=0;$("main").scrollTop=0}}
 else if(k){sel=k.dataset.id;file=byId[sel].arquivo;render();if(innerWidth>1000)$("#info").scrollTop=0;if(innerWidth<=1000||e.target.closest(".chip"))(innerWidth<=1000?$("#info"):document.querySelector(".blk.on")).scrollIntoView({behavior:"smooth",block:"start"})}});
document.addEventListener("keydown",e=>{if(e.key==="Enter"&&e.target.dataset&&e.target.dataset.id)e.target.click()});
render();})();