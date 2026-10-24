export function updateHardwareGauges(cpu, ram, disk) {
  const cpuEl = document.getElementById("cpu-txt");
  const ramEl = document.getElementById("ram-txt");
  const diskEl = document.getElementById("disk-txt");

  if (cpuEl) cpuEl.innerText = `${cpu}%`;
  if (ramEl) ramEl.innerText = `${ram}%`;
  if (diskEl) diskEl.innerText = `${disk}%`;
}
