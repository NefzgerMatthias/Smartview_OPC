function formatValue(tag) {
  const v = tag?.value;
  const unit = tag?.unit ?? "";
  if (typeof v === "boolean") return v ? "Ein" : "Aus";
  if (v === null || v === undefined) return "—";
  return `${v}${unit ? " " + unit : ""}`;
}

function tagTypeBadge(tag) {
  const type = (tag?.type ?? "").toLowerCase();
  if (type === "analog") return `<span class="badge text-bg-info">Analog</span>`;
  if (type === "digital") return `<span class="badge text-bg-warning">Digital</span>`;
  return `<span class="badge text-bg-secondary">Unbekannt</span>`;
}

export function renderTags(tagGridEl, tagsObj) {
  const entries = Object.entries(tagsObj ?? {});
  if (entries.length === 0) {
    tagGridEl.innerHTML = `<div class="text-body-secondary">Keine Tags verfügbar.</div>`;
    return;
  }

  tagGridEl.innerHTML = entries.map(([name, tag]) => {
    return `
      <div class="tag-card">
        <div class="d-flex align-items-start justify-content-between gap-2">
          <div class="tag-name">${name}</div>
          ${tagTypeBadge(tag)}
        </div>
        <div class="tag-value">${formatValue(tag)}</div>
        <div class="tag-meta">raw: ${JSON.stringify(tag)}</div>
      </div>
    `.trim();
  }).join("");
}

export function setStatus(badgeEl, status) {
  // status: "ok" | "error" | "idle"
  badgeEl.className = "badge";
  if (status === "ok") {
    badgeEl.classList.add("text-bg-success", "badge-dot");
    badgeEl.textContent = "Online";
  } else if (status === "error") {
    badgeEl.classList.add("text-bg-danger", "badge-dot");
    badgeEl.textContent = "Fehler";
  } else {
    badgeEl.classList.add("text-bg-secondary");
    badgeEl.textContent = "Gestoppt";
  }
}

export function setLastUpdate(el) {
  const now = new Date();
  el.textContent = now.toLocaleTimeString();
}