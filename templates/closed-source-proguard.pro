# Optional FRAGMENT for your OWN classic Bukkit/Paper plugin, not a ready build.
# Replace example classes/packages with real external roots. Set verified input,
# output and library JARs via the existing build. Requires a compatible ProGuard.
# Start with name obfuscation only; enable shrinking/optimization separately
# after final-artifact tests and a complete dynamic-reachability inventory.
-dontshrink
-dontoptimize

# Keep actual loader entry point, constructor and lifecycle.
-keep class com.example.plugin.ExamplePlugin {
    public <init>();
    public void onLoad();
    public void onEnable();
    public void onDisable();
}

# Conservative reflection boundary EXAMPLES: use only real project packages.
# Narrow further only after checking all reflective/annotation discovery paths.
-keep class com.example.plugin.listener.** { *; }
-keep class com.example.plugin.api.** { public protected *; }

# Preserve annotations/signatures needed by reflection, frameworks and consumers.
# Retain line numbers for support; store mappings privately per build.
-keepattributes Signature,Exceptions,InnerClasses,EnclosingMethod,*Annotation*,SourceFile,LineNumberTable

# Required where Kotlin reflection/public Kotlin consumers need adapted metadata;
# verify exact tool/compiler compatibility and keep required classes/members too.
-keep class kotlin.Metadata

# Configure an access-controlled mapping output outside the distribution JAR.
# Add project-specific services/serializers/constructors/JNI and integration roots.
# No ignorewarnings, blanket dontwarn or automatic rewriting of configs/IDs.
