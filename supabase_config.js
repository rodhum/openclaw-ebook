// Configuración Central de Supabase para el e-Book OpenClaw
// Actualizado: 2026-09-23 por Isaac (Data Admin)
// Proyecto: Leads e-Book (dferpyrtqdkssfnajayum)

const SUPABASE_CONFIG = {
  url: "https://dferpyrtqdkssfnajayum.supabase.co",
  anonKey: "YOUR_ANON_KEY_HERE"  // ⚠️ HUMBERTO: Reemplazar con la anon key completa del dashboard
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
console.log('🔑 Key configurada:', SUPABASE_CONFIG.anonKey !== 'YOUR_ANON_KEY_HERE' ? 'Sí' : '❌ NO - Falta actualizar');
