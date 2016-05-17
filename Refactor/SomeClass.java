package oracle;

public class SomeClass {

    public String getNomCache(String codeApplication, String nom,
                               String valeur, String codeLangue) {
        StringBuffer nomCompletCache = new StringBuffer();

        if ((codeApplication != null) && (getCodeApplication() != null) &&
            !codeApplication.equals(getCodeApplication())) {
            nomCompletCache.append(codeApplication);
            nomCompletCache.append(".");
        }

        nomCompletCache.append(nom);

        if (valeur != null) {
            nomCompletCache.append(".");
            nomCompletCache.append(valeur);
        }

        if (codeLangue != null) {
            nomCompletCache.append(".");
            nomCompletCache.append(codeLangue);
        }

        return nomCompletCache.toString();
    }

    /** méthode requise pour le bien de l'exemple */
    private String getCodeApplication() {
        // return GestionSecurite.getInstance().getCodeApplication();
        return "codeApp";
    }

}
