import { fetchTags } from "./api.js";
import { renderTags, setStatus, setLastUpdate } from "./ui.js";

const els = {
  tagGrid: document.getElementById("tagGrid"),
  statusBadge: document.getElementById("statusBadge"),
  lastUpdate: document.getElementById("lastUpdate"),
  backendUrl: document.getElementById("backendUrl"),
  pollMs: document.getElementById("pollMs"),
  btnStart: document.getElementById("btnStart"),
  btnStop: document.getElementById("btnStop"),
};

let timerId = null;

async function tick() {
  const baseUrl = els.backendUrl.value.trim();
  try {
    const tags = await fetchTags(baseUrl);
    renderTags(els.tagGrid, tags);
    setStatus(els.statusBadge, "ok");
    setLastUpdate(els.lastUpdate);
  } catch (err) {
    console.error(err);
    setStatus(els.statusBadge, "error");
  }
}

function start() {
  stop();
  setStatus(els.statusBadge, "idle");
  tick();

  const ms = Math.max(200, Number(els.pollMs.value) || 1000);
  timerId = setInterval(tick, ms);

  els.btnStart.disabled = true;
  els.btnStop.disabled = false;
}

function stop() {
  if (timerId !== null) {
    clearInterval(timerId);
    timerId = null;
  }
  els.btnStart.disabled = false;
  els.btnStop.disabled = true;
  setStatus(els.statusBadge, "idle");
}

els.btnStart.addEventListener("click", start);
els.btnStop.addEventListener("click", stop);

// Optional: autostart
start();