(function () {
  const typeEl = document.getElementById("id_type");
  const sizeEl = document.getElementById("id_size");
  const out = document.getElementById("js-price-preview");

  if (!typeEl || !sizeEl || !out) return;

  const base = { logo: 30, poster: 40, icon: 20 };
  const mult = { S: 1.0, M: 1.5, L: 2.0 };

  function calc() {
    const t = typeEl.value;
    const s = sizeEl.value;
    if (!base[t] || !mult[s]) { out.textContent = ""; return; }
    const price = (base[t] * mult[s]).toFixed(2);
    out.textContent = `$${price} (preview)`;
  }

  typeEl.addEventListener("change", calc);
  sizeEl.addEventListener("change", calc);
  calc();
})();
