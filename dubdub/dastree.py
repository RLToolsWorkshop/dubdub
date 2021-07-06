from datetime import datetime
from pathlib import Path
from typing import List

from dubdub import create_model, dataclass


@dataclass
class User:
    id: int
    name: str = "John Doe"
    signup_ts: datetime = None


@dataclass
class GenerateAST:
    def main(self, args: List[str]):
        """
        Important Link: https://pydantic-docs.helpmanual.io/usage/models/#dynamic-model-creation
        ---
        defineAst(outputDir, "Expr", Arrays.asList(
            "Binary   : Expr left, Token operator, Expr right",
            "Grouping : Expr expression",
            "Literal  : Object value",
            "Unary    : Token operator, Expr right"
        ));
        """

    def define_ast(self, output_directory: Path, base_name: str, types: List[str]):
        """
        String path = outputDir + "/" + baseName + ".java";
        PrintWriter writer = new PrintWriter(path, "UTF-8");

        writer.println("package com.craftinginterpreters.lox;");
        writer.println();
        writer.println("import java.util.List;");
        writer.println();
        writer.println("abstract class " + baseName + " {");

        for (String type : types) {
        String className = type.split(":")[0].trim();
        String fields = type.split(":")[1].trim();
        defineType(writer, baseName, className, fields);
        }
        writer.println("}");
        writer.close();
        """


"""

public class GenerateAst {
  public static void main(String[] args) throws IOException {
    if (args.length != 1) {
      System.err.println("Usage: generate_ast <output directory>");
      System.exit(64);
    }
    
    String outputDir = args[0];
    defineAst(outputDir, "Expr", Arrays.asList(
        "Binary   : Expr left, Token operator, Expr right",
        "Grouping : Expr expression",
        "Literal  : Object value",
        "Unary    : Token operator, Expr right"
    ));
  }
  
  
    private static void defineAst(
      String outputDir, String baseName, List<String> types)
      throws IOException {
    String path = outputDir + "/" + baseName + ".java";
    PrintWriter writer = new PrintWriter(path, "UTF-8");

    writer.println("package com.craftinginterpreters.lox;");
    writer.println();
    writer.println("import java.util.List;");
    writer.println();
    writer.println("abstract class " + baseName + " {");
    
    for (String type : types) {
      String className = type.split(":")[0].trim();
      String fields = type.split(":")[1].trim(); 
      defineType(writer, baseName, className, fields);
    }
    writer.println("}");
    writer.close();
  }
}

"""

if __name__ == "__main__":
    user = User(id="42", signup_ts="2032-06-21T12:00")
    print(user)
