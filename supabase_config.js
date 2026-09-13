// Configuración Central de Supabase para el e-Book OpenClaw
const SUPABASE_CONFIG = {
  url: "https://pfthfyxamzgiruflfooo.supabase.co",
  anonKey: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBmdGhmeXhhbXpnaXJ1Zmxmb29vIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODY5NzI4MDksImV4cCI6MjEwMjU0ODgwOX0.7WHOYPkIxn80HCss79-vtVdDVE0VWVg4cQRLxh3Q0L8"
};

// Inicializador del cliente de Supabase (requiere @supabase/supabase-js)
function getSupabaseClient() {
  if (typeof supabase !== 'undefined' && supabase.createClient) {
    return supabase.createClient(SUPABASE_CONFIG.url, SUPABASE_CONFIG.anonKey);
  }
  return null;
}
