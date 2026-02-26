import { cpSync, rmSync, existsSync, readdirSync } from 'node:fs';
import { execSync } from 'node:child_process';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const STATIC_REPO = 'https://github.com/1511170/adricrisrueda-static.git';
const TEMP_DIR = join(tmpdir(), 'adricrisrueda-static-deploy');

console.log('🚀 Deploying to static repo...\n');

try {
  // Clean temp directory if exists
  if (existsSync(TEMP_DIR)) {
    rmSync(TEMP_DIR, { recursive: true, force: true });
  }

  // Clone static repo
  console.log('📦 Cloning static repo...');
  execSync(`git clone ${STATIC_REPO} "${TEMP_DIR}"`, { stdio: 'inherit' });

  // Copy dist files
  console.log('📄 Copying build files...');
  const distPath = join(process.cwd(), 'dist');
  
  // List files in dist (for debugging)
  const distFiles = readdirSync(distPath);
  console.log('Files in dist:', distFiles);

  // Copy all files from dist to temp repo (excluding .git)
  cpSync(distPath, TEMP_DIR, { recursive: true, force: true });

  // Configure git (only if not already set)
  try {
    execSync('git config user.email "adriana@adricrisrueda.com"', { 
      cwd: TEMP_DIR, 
      stdio: 'ignore' 
    });
    execSync('git config user.name "Adriana Cris"', { 
      cwd: TEMP_DIR, 
      stdio: 'ignore' 
    });
  } catch (e) {
    // Already configured
  }

  // Add and commit
  console.log('✅ Committing changes...');
  execSync('git add -A', { cwd: TEMP_DIR, stdio: 'inherit' });
  
  const status = execSync('git status --porcelain', { cwd: TEMP_DIR, encoding: 'utf8' });
  
  if (status.trim()) {
    execSync('git commit -m "Build: Actualización automática desde código Astro"', { 
      cwd: TEMP_DIR, 
      stdio: 'inherit' 
    });
    
    // Push
    console.log('🚀 Pushing to static repo...');
    execSync('git push', { cwd: TEMP_DIR, stdio: 'inherit' });
    console.log('\n✅ Deploy completed successfully!');
  } else {
    console.log('ℹ️ No changes to deploy.');
  }

} catch (error) {
  console.error('❌ Deploy failed:', error.message);
  process.exit(1);
} finally {
  // Clean up
  if (existsSync(TEMP_DIR)) {
    rmSync(TEMP_DIR, { recursive: true, force: true });
  }
}
