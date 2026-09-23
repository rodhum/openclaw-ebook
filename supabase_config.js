// Configuración Central de Supabase para el e-Book OpenClaw
// Actualizado: 2026-09-23 por Isaac (Data Admin)
// Proyecto: Leads e-Book (dferpvtqdskssfnajayum)

const SUPABASE_CONFIG = {
  url: "https://dferpvtqdskssfnajayum.supabase.co",
  anonKey: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRmZXJwdnRxZGtzc2ZuYWpheXVtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTAxOTExNDUsImV4cCI6MjEwNTc2NzE0NX0.fCxKZZb1fj4cLfDS22-3K48BmDJkflVhJorXLse_QZA"
};

// Inicializador del cliente de Supabase (requiere @supabase/supabase-js)
function getSupabaseClient() {
  if (typeof supabase !== 'undefined' && supabase.createClient) {
    return supabase.createClient(SUPABASE_CONFIG.url, SUPABASE_CONFIG.anonKey);
  }
  console.error('Supabase client library no está cargada. Verifica que @supabase/supabase-js esté incluido.');
  return null;
}

// Log de inicialización
console.log('✅ Supabase config cargado');
console.log('📊 Proyecto:', SUPABASE_CONFIG.url);
console.log('🔑 Key configurada: Sí');
