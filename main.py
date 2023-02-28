import os
import warnings
from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText

from openfabric_pysdk.context import OpenfabricExecutionRay
from openfabric_pysdk.loader import ConfigClass
from time import time
from haystack.nodes import FARMReader
# if you are running from github, please download the model from the drive link
# https://drive.google.com/drive/folders/1OBRAIGMLTM6rckZLY-0vmKPsWeu2JUOn?usp=share_link
new_reader = FARMReader(model_name_or_path="distilbert-base-cased-distilled-squad/")
context = '''The branches of science, also referred to as sciences, scientific fields or scientific disciplines, are commonly divided into three major groups:

Formal sciences: the study of formal systems, such as those under the branches of logic and mathematics, which use an a priori, as opposed to empirical, methodology.
Natural sciences: the study of natural phenomena (including cosmological, geological, physical, chemical, and biological factors of the universe). Natural science can be divided into two main branches: physical science and life science (or biology).
Social sciences: the study of human behavior in its social and cultural aspects.[1]
Scientific knowledge must be based on observable phenomena and must be capable of being verified by other researchers working under the same conditions.[2] This verifiability may well vary even within a scientific discipline.[3][4]

Natural, social, and formal science make up the fundamental sciences, which form the basis of interdisciplinarity- and applied sciences such as engineering and medicine. Specialized scientific disciplines that exist in multiple categories may include parts of other scientific disciplines but often possess their own terminologies and expertises.[5]


The formal sciences are the branches of science that are concerned with formal systems, such as logic, mathematics, theoretical computer science, information theory, systems theory, decision theory, statistics.

Unlike other branches, the formal sciences are not concerned with the validity of theories based on observations in the real world (empirical knowledge), but rather with the properties of formal systems based on definitions and rules. Hence there is disagreement on whether the formal sciences actually constitute as a science. Methods of the formal sciences are, however, essential to the construction and testing of scientific models dealing with observable reality,[6] and major advances in formal sciences have often enabled major advances in the empirical sciences.


Logic (from Greek: λογική, logikḗ, 'possessed of reason, intellectual, dialectical, argumentative')[7][8][note 1] is the systematic study of valid rules of inference, i.e. the relations that lead to the acceptance of one proposition (the conclusion) on the basis of a set of other propositions (premises). More broadly, logic is the analysis and appraisal of arguments.[9]

It has traditionally included the classification of arguments; the systematic exposition of the logical forms; the validity and soundness of deductive reasoning; the strength of inductive reasoning; the study of formal proofs and inference (including paradoxes and fallacies); and the study of syntax and semantics.

Historically, logic has been studied in philosophy (since ancient times) and mathematics (since the mid-19th century). More recently, logic has been studied in cognitive science, which draws on computer science, linguistics, philosophy and psychology, among other disciplines.


Information science is an academic field which is primarily concerned with analysis, collection, classification, manipulation, storage, retrieval, movement, dissemination, and protection of information. Practitioners within and outside the field study the application and the usage of knowledge in organizations in addition to the interaction between people, organizations, and any existing information systems with the aim of creating, replacing, improving, or understanding the information systems.

Mathematics, in the broadest sense, is just a synonym of formal science; but traditionally mathematics means more specifically the coalition of four areas: arithmetic, algebra, geometry, and analysis, which are, to some degree, the study of quantity, structure, space, and change respectively.


Statistics is the study of the collection, organization, and interpretation of data.[10][11] It deals with all aspects of this, including the planning of data collection in terms of the design of surveys and experiments.[10]

A statistician is someone who is particularly well versed in the ways of thinking necessary for the successful application of statistical analysis. Such people have often gained this experience through working in any of a wide number of fields. There is also a discipline called mathematical statistics, which is concerned with the theoretical basis of the subject.

The word statistics, when referring to the scientific discipline, is singular, as in "Statistics is an art."[12] This should not be confused with the word statistic, referring to a quantity (such as mean or median) calculated from a set of data,[13] whose plural is statistics ("this statistic seems wrong" or "these statistics are misleading").


Systems theory is the transdisciplinary study of systems in general, to elucidate principles that can be applied to all types of systems in all fields of research. The term does not yet have a well-established, precise meaning, but systems theory can reasonably be considered a specialization of systems thinking and a generalization of systems science. The term originates from Bertalanffy's General System Theory (GST) and is used in later efforts in other fields, such as the action theory of Talcott Parsons and the sociological autopoiesis of Niklas Luhmann.

In this context the word systems is used to refer specifically to self-regulating systems, i.e. that are self-correcting through feedback. Self-regulating systems are found in nature, including the physiological systems of our body, in local and global ecosystems, and climate.

Decision theory (or the theory of choice not to be confused with choice theory) is the study of an agent's choices.[14] Decision theory can be broken into two branches: normative decision theory, which analyzes the outcomes of decisions or determines the optimal decisions given constraints and assumptions, and descriptive decision theory, which analyzes how agents actually make the decisions they do.

Decision theory is closely related to the field of game theory[15] and is an interdisciplinary topic, studied by economists, statisticians, psychologists, biologists,[16] political and other social scientists, philosophers,[17] and computer scientists.

Empirical applications of this rich theory are usually done with the help of statistical and econometric methods.

Theoretical computer science (TCS) is a subset of general computer science and mathematics that focuses on more mathematical topics of computing, and includes the theory of computation.

It is difficult to circumscribe the theoretical areas precisely. The ACM's Special Interest Group on Algorithms and Computation Theory (SIGACT) provides the following description:[18]

TCS covers a wide variety of topics including algorithms, data structures, computational complexity, parallel and distributed computation, probabilistic computation, quantum computation, automata theory, information theory, cryptography, program semantics and verification, machine learning, computational biology, computational economics, computational geometry, and computational number theory and algebra. Work in this field is often distinguished by its emphasis on mathematical technique and rigor.


Natural science is a branch of science concerned with the description, prediction, and understanding of natural phenomena, based on empirical evidence from observation and experimentation. Mechanisms such as peer review and repeatability of findings are used to try to ensure the validity of scientific advances.

Natural science can be divided into two main branches: life science and physical science. Life science is alternatively known as biology, and physical science is subdivided into branches: physics, chemistry, astronomy and Earth science. These branches of natural science may be further divided into more specialized branches (also known as fields)


Physical science is an encompassing term for the branches of natural science that study non-living systems, in contrast to the life sciences. However, the term "physical" creates an unintended, somewhat arbitrary distinction, since many branches of physical science also study biological phenomena. There is a difference between physical science and physics.


Physics (from Ancient Greek: φύσις, romanized: physis, lit. 'nature') is a natural science that involves the study of matter[note 2] and its motion through spacetime, along with related concepts such as energy and force.[20] More broadly, it is the general analysis of nature, conducted in order to understand how the universe behaves.[21][22][note 3]

Physics is one of the oldest academic disciplines, perhaps the oldest through its inclusion of astronomy.[note 4] Over the last two millennia, physics was a part of natural philosophy along with chemistry, certain branches of mathematics, and biology, but during the Scientific Revolution in the 16th century, the natural sciences emerged as unique research programs in their own right.[note 5] Certain research areas are interdisciplinary, such as biophysics and quantum chemistry, which means that the boundaries of physics are not rigidly defined. In the nineteenth and twentieth centuries physicalism emerged as a major unifying feature of the philosophy of science as physics provides fundamental explanations for every observed natural phenomenon. New ideas in physics often explain the fundamental mechanisms of other sciences, while opening to new research areas in mathematics and philosophy.

Chemistry (the etymology of the word has been much disputed)[note 6] is the science of matter and the changes it undergoes. The science of matter is also addressed by physics, but while physics takes a more general and fundamental approach, chemistry is more specialized, being concerned by the composition, behavior (or reaction), structure, and properties of matter, as well as the changes it undergoes during chemical reactions.[23][24] It is a physical science which studies various substances, atoms, molecules, and matter (especially carbon based). Example sub-disciplines of chemistry include: biochemistry, the study of substances found in biological organisms; physical chemistry, the study of chemical processes using physical concepts such as thermodynamics and quantum mechanics; and analytical chemistry, the analysis of material samples to gain an understanding of their chemical composition and structure. Many more specialized disciplines have emerged in recent years, e.g. neurochemistry the chemical study of the nervous system.


Earth science (also known as geoscience, the geosciences or the Earth sciences) is an all-embracing term for the sciences related to the planet Earth.[25] It is arguably a special case in planetary science, the Earth being the only known life-bearing planet. There are both reductionist and holistic approaches to Earth sciences. The formal discipline of Earth sciences may include the study of the atmosphere, hydrosphere, lithosphere, and biosphere, as well as the solid earth. Typically Earth scientists will use tools from physics, chemistry, biology, geography, chronology and mathematics to build a quantitative understanding of how the Earth system works, and how it evolved to its current state.


Geology (from the Ancient Greek γῆ, gē ("earth") and -λoγία, -logia, ("study of", "discourse")[26][27]) is an Earth science concerned with the solid Earth, the rocks of which it is composed, and the processes by which they change over time. Geology can also include the study of the solid features of any terrestrial planet or natural satellite such as Mars or the Moon. Modern geology significantly overlaps all other Earth sciences, including hydrology and the atmospheric sciences, and so is treated as one major aspect of integrated Earth system science and planetary science.


Oceanography, or marine science, is the branch of Earth science that studies the ocean. It covers a wide range of topics, including marine organisms and ecosystem dynamics; ocean currents, waves, and geophysical fluid dynamics; plate tectonics and the geology of the seafloor; and fluxes of various chemical substances and physical properties within the ocean and across its boundaries. These diverse topics reflect multiple disciplines that oceanographers blend to further knowledge of the world ocean and understanding of processes within it: biology, chemistry, geology, meteorology, and physics as well as geography.


Meteorology is the interdisciplinary scientific study of the atmosphere. Studies in the field stretch back millennia, though significant progress in meteorology did not occur until the 17th century. The 19th century saw breakthroughs occur after observing networks developed across several countries. After the development of the computer in the latter half of the 20th century, breakthroughs in weather forecasting were achieved.


Space science is the study of everything in outer space.[28] This has sometimes been called astronomy, but recently astronomy has come to be regarded as a division of broader space science, which has grown to include other related fields,[29] such as studying issues related to space travel and space exploration (including space medicine), space archaeology[30] and science performed in outer space (see space research).


Life science, also known as biology, is the natural science that studies life such as microorganisms, plants, and animals including human beings, – including their physical structure, chemical processes, molecular interactions, physiological mechanisms, development, and evolution.[31] Despite the complexity of the science, certain unifying concepts consolidate it into a single, coherent field. Biology recognizes the cell as the basic unit of life, genes as the basic unit of heredity, and evolution as the engine that propels the creation and extinction of species. Living organisms are open systems that survive by transforming energy and decreasing their local entropy[32] to maintain a stable and vital condition defined as homeostasis.[33]


Biochemistry, or biological chemistry, is the study of chemical processes within and relating to living organisms.[34] It is a sub-discipline of both biology and chemistry, and from a reductionist point of view it is fundamental in biology. Biochemistry is closely related to molecular biology, cell biology, genetics, and physiology.


Microbiology is the study of microorganisms, those being unicellular (single cell), multicellular (cell colony), or acellular (lacking cells). Microbiology encompasses numerous sub-disciplines including virology, bacteriology, protistology, mycology, immunology and parasitology.


Botany, also called plant science(s), plant biology or phytology, is the science of plant life and a branch of biology. Traditionally, botany has also included the study of fungi and algae by mycologists and phycologists respectively, with the study of these three groups of organisms remaining within the sphere of interest of the International Botanical Congress. Nowadays, botanists (in the strict sense) study approximately 410,000 species of land plants of which some 391,000 species are vascular plants (including approximately 369,000 species of flowering plants),[35] and approximately 20,000 are bryophytes.[36]


Zoology (/zoʊˈɒlədʒi/)[note 7] is the branch of biology that studies the animal kingdom, including the structure, embryology, evolution, classification, habits, and distribution of all animals, both living and extinct, and how they interact with their ecosystems. The term is derived from Ancient Greek ζῷον, zōion, i.e. "animal" and λόγος, logos, i.e. "knowledge, study".[37] Some branches of zoology include: anthrozoology, arachnology, archaeozoology, cetology, embryology, entomology, helminthology, herpetology, histology, ichthyology, malacology, mammalogy, morphology, nematology, ornithology, palaeozoology, pathology, primatology, protozoology, taxonomy, and zoogeography.


Ecology (from Greek: οἶκος, "house", or "environment"; -λογία, "study of")[note 8] is a branch of biology[38] concerning interactions among organisms and their biophysical environment, which includes both biotic and abiotic components. Topics of interest include the biodiversity, distribution, biomass, and populations of organisms, as well as cooperation and competition within and between species. Ecosystems are dynamically interacting systems of organisms, the communities they make up, and the non-living components of their environment. Ecosystem processes, such as primary production, pedogenesis, nutrient cycling, and niche construction, regulate the flux of energy and matter through an environment. These processes are sustained by organisms with specific life history traits.


Social science is the branch of science devoted to the study of societies and the relationships among individuals within those societies. The term was formerly used to refer to the field of sociology, the original "science of society", established in the 19th century. In addition to sociology, it now encompasses a wide array of academic disciplines, including anthropology, archaeology, economics, human geography, linguistics, political science, and psychology.

Positivist social scientists use methods resembling those of the natural sciences as tools for understanding society, and so define science in its stricter modern sense. Interpretivist social scientists, by contrast, may use social critique or symbolic interpretation rather than constructing empirically falsifiable theories. In modern academic practice, researchers are often eclectic, using multiple methodologies (for instance, by combining both quantitative and qualitative research). The term "social research" has also acquired a degree of autonomy as practitioners from various disciplines share in its aims and methods.


Applied science is the use of existing scientific knowledge to achieve practical goals, like technology or inventions.

Within natural science, disciplines that are basic science develop basic information to explain and perhaps predict phenomena in the natural world. Applied science is the use of scientific processes and knowledge as the means to achieve a particularly practical or useful result. This includes a broad range of applied science-related fields, including engineering and medicine.

Applied science can also apply formal science, such as statistics and probability theory, as in epidemiology. Genetic epidemiology is an applied science applying both biological and statistical methods.
'''
############################################################
# Callback function called on update config
############################################################
def config(configuration: ConfigClass):
    # TODO Add code here
    pass


############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    output = []
    for text in request.text:
        # TODO Add code here
        answers = new_reader.predict_on_texts(text,[context])
        response =  answers['answers'][0].answer
        output.append(response)

    return SimpleText(dict(text=output))
