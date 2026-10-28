import javax.tools.ToolProvider;
import java.net.URLClassLoader;
import java.nio.file.*;
import java.util.Comparator;

/** Compile/run the pure example with an available JDK compiler; no downloads or Minecraft. */
public class CheckJavaExample {
    public static void main(String[] args) throws Exception {
        Path root = (args.length == 0 ? Path.of(".") : Path.of(args[0])).toAbsolutePath().normalize();
        var compiler = ToolProvider.getSystemJavaCompiler();
        if (compiler == null) throw new IllegalStateException("Run with a JDK that includes jdk.compiler");
        Path output = Files.createTempDirectory("minecraft-skill-example-");
        try {
            int result = compiler.run(null, System.out, System.err, "--release", "21", "-d", output.toString(),
                    root.resolve("examples/java/SessionGate.java").toString(),
                    root.resolve("tests/SessionGateJavaTest.java").toString());
            if (result != 0) throw new IllegalStateException("Compilation failed: " + result);
            try (var loader = new URLClassLoader(new java.net.URL[]{output.toUri().toURL()})) {
                loader.loadClass("examples.SessionGateJavaTest").getMethod("main", String[].class)
                        .invoke(null, (Object) new String[0]);
            }
            System.out.println("Java example compiled with --release 21; runtime: " + Runtime.version());
        } finally {
            try (var paths = Files.walk(output)) {
                for (Path path : paths.sorted(Comparator.reverseOrder()).toList()) Files.delete(path);
            }
        }
    }
}
