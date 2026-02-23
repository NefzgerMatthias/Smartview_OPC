export async function fetchTags(baseUrl) {
  const url = `${baseUrl.replace(/\/$/, "")}/api/tags`;
  const res = await fetch(url, { method: "GET" });

  if (!res.ok) {
    const text = await res.text().catch(() => "");
    throw new Error(`HTTP ${res.status} beim Laden von /api/tags ${text ? "- " + text : ""}`);
  }
  return await res.json();}