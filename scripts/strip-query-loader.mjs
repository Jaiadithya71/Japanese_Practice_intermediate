// Test-only ESM loader: strips cache-busting '?v=...' query strings from
// relative module specifiers so Node can resolve them (browsers accept them).
export async function resolve(specifier, context, nextResolve) {
  if (specifier.startsWith('./') || specifier.startsWith('../')) {
    const q = specifier.indexOf('?');
    if (q !== -1) return nextResolve(specifier.slice(0, q), context);
  }
  return nextResolve(specifier, context);
}
